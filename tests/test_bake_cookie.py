def test_bake_project(cookies):
    extra_context = {
        "full_name": "Foo Bar",
        "email": "foo@bar.com",
        "github_username": "foobar",
        "project_name": "Test Project",
        "project_short_description": "my test project description",
    }

    result = cookies.bake(extra_context=extra_context)

    print(result.project)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "test_project"
    assert result.project.isdir()
